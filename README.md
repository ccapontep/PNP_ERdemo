# PNP ER demo

This folder contains a full example of PNP application using ROS actions.

Organization of the folders:

* `er_pddl`: PDDL domain and problem descriptions for plan generation
* `er_action` and `er_action_msgs`: implementation of basic actions (no PNP code)
* `er_pnp`: plans and scripts to run plans (PNP ActionServer code)
* `er_demo`: overall demo launch

## Docker image

It is suggested to run these examples in docker containers. 
Follow instructions in [PetriNetPlans/docker](/docker) to build 
PNP docker image for Ubuntu 16.04 and ROS kinetic.
Make sure you can succesfully run the PNP image
```ub1604_kinetic_pnp:1.0```


Then, build a new docker image including this demo.

        ./build.bash

and run the image

        ./run.bash

Note: if you want to link your local directories of PNP and this demo in the docker image,
use instead

        ./run_dev.bash

in this way you can develop the demo within the docker container.


## Link and compile this demo

```diff
- Note: not needed if you are using the docker image. -
```

Make sure PNP and PNPros have been installed and build ROS packages in this folder.

ADD er_pnp /home/robot/src/er_pnp
ADD er_demo /home/robot/src/er_demo
ADD er_pddl /home/robot/src/er_pddl

Example:

        cd ~/ros/catkin_ws/src
        ln -s <path_to_this_repository>/er_pnp . 
        ln -s <path_to_this_repository>/er_demo .
        cd ..
        catkin_make


## Running the demo

Start the demo

        roscd er_demo/scripts
        ./start_demo.bash 

Run a plan

        roscd er_pnp/scripts
        ./runplan.bash sequence_loop

Other plans to test available in `er_pnp/plans` folder.

Stop the current plan

        roscd er_pnp/scripts
        ./runplan.bash stop

Quit the simulation

        rosnode kill -a


## Plan generation

Plans can be generated with PDDL planners. One such planner you can use is http://planning.domains/

1. To create your plans, create a domain and problem in the editor http://editor.planning.domains/

   Resources and examples to write your PDDL plan:

	http://users.cecs.anu.edu.au/~patrik/pddlman/writing.html

	http://www.cs.toronto.edu/~sheila/384/w11/Assignments/A3/veloso-PDDL_by_Example.pdf


2. To compute/run your plan, select "Solve" and choose your domain, problem and chosen planner. A tab will open with your plan output as a .txt file. 

3. Save your domain, problem, and plan output to your pnp-demo pddl folder (e.g. er_pnp-demo/er_pddl). Rename your plan output to extension .pddlout (e.g. ER.pddlout).



Generate a PNP from PDDL output file

        cd ~/src/er_pddl
        pnpgen_linear ER.pddlout

Note: file format is detected from file name extension, for PDDL output
make sure your file extention is ```.pddlout```.

This will generate the PNP ```ER.pnml``` corresponding to this plan.

To visualize the generated PNP, use Jarp

        jarp.sh

and then open the generated ```pnml``` file.	



## Run generated plans

To run a new plan generated from a PDDL domain, you need to execute these two steps.

1) Implement all the actions referred in the plan.

Create file of action and add in it the goal, result, and feedback needed for the action

        cd er_action_msgs/action
	touch Dialog.action
	
In CMakeLists.txt add your action and remove others from: 

	add_action_files( ~~Turn.action~~ 
			  Dialog.action)
				  
All other items are kept the same as the example in er_action_msgs for CMakeLists.txt and package.xml. 
If other dependencies are needed to build or run, add them into these files.

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

Create your action server and client with the action message created above. 

Resources for examples:
- http://wiki.ros.org/actionlib (general, both C++ and Python)
- http://wiki.ros.org/actionlib_tutorials/Tutorials/SimpleActionServer%28ExecuteCallbackMethod%29	(Python Action Server)
- http://wiki.ros.org/actionlib_tutorials/Tutorials/Writing%20a%20Simple%20Action%20Client%20%28Python%29 	(Python Action Client)

Make your files executables so they can run using:

	chmod +x filename.py

Update CMakeList.txt, package.xml, and robot.launch files so it has no duplicate actions and names (replace any 'er_action' and 'er_action_msgs' to your own package name).

Build your packages again:
	
	cd ~/playground/er_pnp-demo
	./run_dev.bash

Check that your files can run:
	
	rosrun er_action conv2screen_server.py
	rosnode list | grep server
	#output: 	/conv2screen_server

For more info about your node:

	rosnode info /conv2screen_server

To check that the client runs correctly with the server, in another tab:

	rosrun er_action conv2screen_client.py
	#output: 	Result: Hello, how can I help you?


2) Run the action server to manage these actions

        TODO ...

3) Run the new plan

        cp <new_plan> ~/src/er_pnp/plans
        roscd er_pnp/scripts
        ./runplan.bash <new_plan>




## Implementation details

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



