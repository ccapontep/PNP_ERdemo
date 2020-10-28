# PNP ER demo

This folder contains a full example of PNP application using PDDL planning domains and solvers and ROS actions.

Organization of the folders:

* `er_action` and `er_action_msgs`: implementation of basic actions (no PNP code)
* `er_pnp`: plans and scripts to run plans (PNP ActionServer code)

We assume robot or simulator is started externally from this module.

## Docker image

It is suggested to run these examples in docker containers. 
Follow instructions in [PetriNetPlans/docker](/docker) to build 
a PNP docker image for Ubuntu 16.04 and ROS kinetic.
Make sure you can succesfully run the PNP image
```pnp_ub1604_kinetic```


Then, build a new docker image including this demo. Do this only once, otherwise you will build the docker image each time; to update your application after adding changes see below under run_dev.bash

        ./build.bash

and run the image

        ./run.bash

Note: if you want to link your local directories of PNP and this demo in the docker image, use instead

        ./run_dev.bash

in this way you can develop the demo within the docker container. Any time you change any C++ file, you have to compile with:

	cd ros/catkin_ws
	catkin_make
	source devel/setup.bash


## Build ROS packages for this demo

```diff
- Note: not needed if you are using the docker image. -
```

Make sure PNP and PNPros have been installed. Setup and build ROS packages of this repository

Example:

        cd ~/ros/catkin_ws/src
        ln -s <path_to_this_repository>/er_pnp . 
        ln -s <path_to_this_repository>/er_action .
        ln -s <path_to_this_repository>/er_action_msgs .
        cd ..
        catkin_make




## Plan generation

Plans can be generated with PDDL planners using, for example, the web interface provided by [planning.domains](http://planning.domains/)

1. To create your plans, create a domain and problem in the [editor](http://editor.planning.domains/)

    Resources and examples to write your PDDL plan:

    	http://users.cecs.anu.edu.au/~patrik/pddlman/writing.html

    	http://www.cs.toronto.edu/~sheila/384/w11/Assignments/A3/veloso-PDDL_by_Example.pdf


2. To compute/run your plan, select "Solve" and choose your domain, problem and chosen planner. A tab will open with your plan output as a .txt file. 

3. Save your domain, problem, and plan output to your pnp folder (e.g. `er_pnp/plans`). 
Rename your plan output to extension `.pddlout` (e.g. `ER.pddlout`). This step is necessary since
PNP generator will recognize the format of this file from the extension `.pddlout`.


4. [optional] Write execution rules `ER.er`

5. Generate a PNP from PDDL output file and (optional) execution rules 

        roscd er_pnp/plans
        pnpgen_linear ER.pddlout [ER.er]

Note: file format is detected from file name extension, for PDDL output
make sure your file extention is ```.pddlout```.

This will generate the PNP ```ER.pnml``` corresponding to this plan.

To visualize the generated PNP, use Jarp

        jarp.sh

and then open the generated ```pnml``` file.	




## Running the demo

* Start an environment

    Follow instructions in [stage_environments](https://bitbucket.org/iocchi/stage_environments/)

* Start actions

        roslaunch er_action actions.launch

* Start PNP

        roslaunch er_pnp pnp.launch



## Run generated plans


Run the plan generated with `pnpgen` (e.g., `ER.pnml`)

        rosrun er_pnp runplan.bash ER

Stop the current plan

        rosrun er_pnp runplan.bash stop



----

## Implementation details on PNPActionServer

The devlopment of a PNP-based application requires two components:
* domain-independent plan execution monitor `pnp_node` ROS node
* a plan to be executed `<plan>.pnml`
* a domain-specific PNP Action Server implementing actions and conditions 
that will be used by the PNP plan execution monitor

The PNP Action Server is a ROS node inheriting from the domain-independent
class `PNPActionServer` defined in `PNPros` package 
([see PNPActionServer.h](/PNPros/ROS_bridge/pnp_ros/include/pnp_ros/PNPActionServer.h)).

Example:
        
        // definition of action functions

        void action_fn(string params, bool *run) {
          ...
          while ( ... && (*run)) {
            ...
          }
        }

        // definition of condition functions

        int condition_fn(string params) {
          int r = ...; // 0: false, 1: true, -1: unknown
          return r;
        }
        

        // PNP Action server

        class MyPNPActionServer : public PNPActionServer {

          public:

            MyPNPActionServer() : PNPActionServer()  { 
	        
              register_action("action",&action_fn);
              ...
              register_condition("condition",&condition_fn);
              ...
            }

        };




----

## Examples of implementation of actions and conditions


1) Implement all the actions referred in the plan.

Create file of action and add in it the goal, result, and feedback needed for the action

        cd er_action_msgs/action
	touch Dialog.action
	
In CMakeLists.txt add your action and remove others from: 

	add_action_files( ~~Turn.action~~ 
			  Dialog.action)
				  
All other items are kept the same as the example in er_action_msgs for CMakeLists.txt and package.xml. 
If other dependencies are needed to build or run, add them into these files.

Compile your changes:
	cd ros/catkin_ws
	catkin_make
	source devel/setup.bash

To test the action message works run:

	rosmsg list | grep Dialog
	
Output should be in the form:

	er_action_msgs/DialogAction
	er_action_msgs/DialogFeedback
	er_action_msgs/DialogGoal
	er_action_msgs/DialogResult
	

Or also test using:
	python -c 'from er_action_msgs.msg import DialogAction; print "Hey, it worked!"' 

--

Create your action server and client with the action message created above. The server can be done either in python or C++ and should be added to location: er_action/src. Make sure your server node is running by adding it to the file robot.launch in location er_action/launch as such:

	<node pkg="er_action" type="dialog_server.py" name="dialog" output="screen" />

The client instead has to be in C++ and added to the file MyActions.cpp in location er_pnp/src. 

Resources for examples:
- http://wiki.ros.org/actionlib (general, both C++ and Python)
- http://wiki.ros.org/actionlib_tutorials/Tutorials/SimpleActionServer%28ExecuteCallbackMethod%29	(C++ Action Server)
- http://wiki.ros.org/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Client%20%28Python%29 	(Python Action Client)

Make your files executables so they can run using:

	chmod +x filename.py

Update CMakeList.txt, package.xml, and robot.launch files so it has no duplicate actions and names (replace any 'er_action' and 'er_action_msgs' to your own package name).

Build your packages again:
	
	cd ~/playground/er_pnp-demo
	./run_dev.bash

Check that your files can run:
	
	rosrun er_action dialog_server.py
	rosnode list | grep server
	#output: 	/dialog_server

For more info about your node:

	rosnode info /dialog_server

To check that the client runs correctly with the server, in another tab:

	rosrun er_action dialog_client.py
	#output: 	Result: Hello, how can I help you?


2) Run the action server to manage these actions

        TODO ...




## Creating a new map

To add your own custom map to the your application, you need a photo of your map from top view that shows each room and walls.

You need to localize your robot so your .yaml file in er_demo/maps is aligned to your .world file. To do this you need to work with rviz, which is already included in the PNP package.

Follow the instruction in section 5.1: http://wiki.ros.org/turtlebot_stage/Tutorials/indigo/Customizing%20the%20Stage%20Simulator

A tutorial for that is: https://www.youtube.com/watch?v=K1ZFkR4YsRQ




