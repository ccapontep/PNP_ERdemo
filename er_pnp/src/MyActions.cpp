#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <actionlib/client/simple_action_client.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <sensor_msgs/LaserScan.h>
//for mapping key of location to coordinates
// #include <map>
#include <iostream>


#include <rp_action_msgs/TurnAction.h>
#include <er_action_msgs/DialogAction.h>
#include <er_action_msgs/ResolveIssueAction.h>

#include <boost/thread/thread.hpp>

#define radians(a) ((a)/180.0*M_PI)

std::string robotname="";

// defined in robotpose.cpp
bool getRobotPose(std::string robotname, double &x, double &y, double &th_rad);

// defined in gotopose.cpp
void exec_gotopose(std::string robotname, float GX, float GY, float GTh, bool *run);

using namespace std;

std::string turn_topic = "turn";
std::string movebase_topic = "move_base";

actionlib::SimpleActionClient<rp_action_msgs::TurnAction> *ac_turn = NULL;
actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> *ac_movebase = NULL;


/*** ACTIONS ***/

void start_gotopose(float GX, float GY, float GTh, bool *run) {

  exec_gotopose(robotname, GX, GY, GTh, run);

}


// Action implementation

void ainit(string params, bool *run) {
  cout << "\n### Executing Init ... " << params << endl;
  // Set turn topic

  float GX=2.0;
  float GY=2.0;
  float GTh=0;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
      cout << "### Finished Init " << endl;
  else
      cout << "### Aborted Init  " << endl;
}

void gotopose(string params, bool *run) {
  cout << "\n### Executing Gotopose ... " << params << endl;

  int i=params.find("_");
  float GX=atof(params.substr(0,i).c_str());
  int j=params.find("_",i+1);
  float GY=atof(params.substr(i+1,j).c_str());
  float GTh=atof(params.substr(j+1).c_str());

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished Gotopose " << endl;
  else
    cout << "### Aborted Gotopose  " << endl;
}

void home(string params, bool *run)
{
  cout << "\n### Executing Home ... " << params << endl;

  float GX=2.0;
  float GY=2.0;
  float GTh=0;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished Home " << endl;
  else
    cout << "### Aborted Home  " << endl;
}

void wave(string params, bool *run) {
    cout << "\n### Executing Wave ... " << params << endl;

    cout << "HELLO FROM " << robotname << " !!!"<<endl;
    boost::this_thread::sleep(boost::posix_time::milliseconds(2000));

    if (*run)
        cout << "### Finished Wave " << endl;
    else
        cout << "### Aborted Wave  " << endl;
}

// #####################################################################3
// Added for ER_pnp-demo


// key mapping from location name to map coordinate
std::map<string, string> initMap() {
  // USED FOR DIS-B1 MAP
    // static std::pair<string, string> data[] = {
    //     std::pair<string, string>("waitingroom", "1.77_0.33_0_0"),
    //     std::pair<string, string>("maincorridor", "2_1.9_0_0"),
    //     std::pair<string, string>("ambulancecorridor", "1.62_3.47_0_0"),
    //     std::pair<string, string>("consultingcorridor", "1.82_8.18_0_0"),
    //     std::pair<string, string>("consultingroom1", "0.71_10.56_0_0"),
    //     std::pair<string, string>("maintriage", "0_1.8_0_0")
    static std::pair<string, string> data[] = {
        std::pair<string, string>("waitingroom", "9.36_9.56_0_0"),
        std::pair<string, string>("maincorridor", "10.39_14.26_0_0"),
        std::pair<string, string>("ambulancecorridor", "27.73_15.51_0_0"),
        std::pair<string, string>("consultingcorridor", "36.56_25.11_0_0"),
        std::pair<string, string>("consultingroom1", "38.2_27.88_0_0"),
        std::pair<string, string>("consultingroom1out", "38.2_25.15_0_0"),
        std::pair<string, string>("consultingroom2", "43.84_27.88_0_0"),
        std::pair<string, string>("consultingroom2out", "43.84_25.15_0_0"),
        std::pair<string, string>("maintriage", "16_19.2_0_0")
    };

    return map<string, string>(data, data + sizeof(data) / sizeof(*data));
}

// To initiate the map, use:
// std::map<string, string> map_loc2coord = initMap();


void moverobot(string params, bool *run) {
  cout << "\n### Executing moveRobot ... " << params << endl;
  // initiate mapping between map location name and coordinate
  std::map<string, string> map_loc2coord = initMap();
  // get index of location name from the plan action
  int nexti = params.find_last_of("_");
  // get the location name
  string nextloc = params.substr(nexti + 1).c_str();
  cout << "\t~ Moving the robot to " << nextloc << " ~\n" << endl;
  // get location coordinate
  string nextcoord = map_loc2coord[nextloc];

  int i=nextcoord.find("_");
  float GX=atof(nextcoord.substr(0,i).c_str());
  int j=nextcoord.find("_",i+1);
  float GY=atof(nextcoord.substr(i+1,j).c_str());
  float GTh=atof(nextcoord.substr(j+1).c_str());
  cout << "\t~ Moving the robot to " << GX << ", " << GY << ", " << GTh << endl;

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished moveRobot " << endl;
  else
    cout << "### Aborted moveRobot  " << endl;
}

void accompanyhuman(string params, bool *run) {
  cout << "\n### Executing accompanyHuman ... " << params << endl;

  // initiate mapping between map location name and coordinate
  std::map<string, string> map_loc2coord = initMap();
  // get index of location name from the plan action
  int nexti = params.find_last_of("_");
  // get the location name
  string nextloc = params.substr(nexti + 1).c_str();
  cout << "\t~ Moving the robot to " << nextloc << " ~\n" << endl;
  // get location coordinate
  string nextcoord = map_loc2coord[nextloc];

  int i=nextcoord.find("_");
  float GX=atof(nextcoord.substr(0,i).c_str());
  int j=nextcoord.find("_",i+1);
  float GY=atof(nextcoord.substr(i+1,j).c_str());
  float GTh=atof(nextcoord.substr(j+1).c_str());

  start_gotopose(GX, GY, GTh, run);

  if (*run)
    cout << "### Finished moveRobot " << endl;
  else
    cout << "### Aborted moveRobot  " << endl;
}

void dialog(string params, bool *run) {
    cout << "\n### Executing Dialog ... " << params << endl;

    // boost::this_thread::sleep(boost::posix_time::milliseconds(2000));
    int i = params.find("_");
    string WhoStartsDialog = params.substr(0,i).c_str();
    int j=params.find("_",i+1);
    string precommand = params.substr(i+1,j).c_str();

    int k = precommand.find("_");
    string command = precommand.substr(0,k).c_str();
    cout << "\t~ Your command is to " << command << " ~\n" << endl;

    // Define the action client (true: we want to spin a thread)
    actionlib::SimpleActionClient<er_action_msgs::DialogAction> ac("dialog_as", false); // false -> need ros::spin()

    // Wait for the action server to come up
    while(!ac.waitForServer(ros::Duration(5.0))){
        ROS_INFO("Waiting for dialog action server to come up");
    }

    // Cancel all goals (JUST IN CASE SOME GOAL WAS NOT CLOSED BEFORE)
    ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec

    // Set the goal
    er_action_msgs::DialogGoal goal;
    if (command == "getpatientdata")
      goal.command = "welcome";

    // Send the goal
    ROS_INFO("Sending goal");
    ac.sendGoal(goal);

    // Wait for termination
    ac.waitForResult(ros::Duration(1.0));

    // Print result
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
      ROS_INFO("Dialog successful");
    else
      ROS_INFO("Dialog failed");

    // Cancel all goals (NEEDED TO ISSUE NEW GOALS LATER)
    ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec

    if (*run)
        cout << "### Finished Dialog " << endl;
    else
        cout << "### Aborted Dialog  " << endl;
}

void resolveissue(string params, bool *run) {
    cout << "\n### Executing ResolveIssue ... " << params << endl;

    // cout << "Can you help me with this issue? "<<endl;
    // boost::this_thread::sleep(boost::posix_time::milliseconds(2000));

    int i = params.find("_");
    string issue = params.substr(0,i).c_str();

    cout << "\t~ Your issue to resolve is " << issue << " ~\n" << endl;

    // Define the action client (true: we want to spin a thread)
    actionlib::SimpleActionClient<er_action_msgs::ResolveIssueAction> ac("resolveIssue_as", false); // false -> need ros::spin()

    // Wait for the action server to come up
    while(!ac.waitForServer(ros::Duration(5.0))){
        ROS_INFO("Waiting for resolve-issue action server to come up");
    }

    // Cancel all goals (JUST IN CASE SOME GOAL WAS NOT CLOSED BEFORE)
    ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec

    // Set the goal
    er_action_msgs::ResolveIssueGoal goal;
    goal.issue = issue;

    // Send the goal
    ROS_INFO("Sending goal");
    ac.sendGoal(goal);

    // Wait for termination
    ac.waitForResult(ros::Duration(1.0));

    // Print result
    if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
      ROS_INFO("Dialog successful");
    else
      ROS_INFO("Dialog failed");

    // Cancel all goals (NEEDED TO ISSUE NEW GOALS LATER)
    ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec

    if (*run)
        cout << "### Finished ResolveIssue " << endl;
    else
        cout << "### Aborted ResolveIssue  " << endl;
}

// Done with ER_pnp-demo actions
// #####################################################################3


void turn360(string params, bool *run) {
#if 0
    cout << "\033[22;31;1m### Executing turn360 ... " << params << "\033[0m" << endl;

    cout << "HELLO FROM " << robotname << " !!!"<<endl;
    boost::this_thread::sleep(boost::posix_time::milliseconds(2000));

    if (*run)
        cout << "### Finished turn360 " << endl;
    else
        cout << "### Aborted turn360  " << endl;
#else
    // Set turn topic
    std::string turn_topic = robotname+"/turn";

    // Define the action client (true: we want to spin a thread)
    actionlib::SimpleActionClient<rp_action_msgs::TurnAction> ac(turn_topic, true);

    // Wait for the action server to come up
    while(!ac.waitForServer(ros::Duration(5.0))){
        ROS_INFO("Waiting for turn action server to come up");
    }

    // Cancel all goals (JUST IN CASE SOME GOAL WAS NOT CLOSED BEFORE)
    ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec

    int counter = 0;

    while (counter++ != 3)
    {
      // Set the goal
      rp_action_msgs::TurnGoal goal;
      goal.target_angle = 120;  // deg
      goal.absolute_relative_flag = "REL";
      goal.max_ang_vel = 45.0;  // deg/s
      goal.name = robotname;

      // Send the goal
      ROS_INFO("Sending goal");
      ac.sendGoal(goal);

      // Wait for termination
      while (!ac.waitForResult(ros::Duration(1.0))) {
	  ROS_INFO_STREAM("Running... [" << ac.getState().toString() << "]");
      }
      ROS_INFO_STREAM("Finished [" << ac.getState().toString() << "]");

      // Print result
      if (ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
	  ROS_INFO("Turn successful");
      else
	  ROS_INFO("Turn failed");

      // Cancel all goals (NEEDED TO ISSUE NEW GOALS LATER)
      ac.cancelAllGoals(); ros::Duration(1).sleep(); // wait 1 sec
    }
#endif
}

void sense1(string params, bool *run) {
  cout << "\n### Executing Sense1 ... " << params << endl;
}



/*** CONDITIONS ***/

int closeToHomeCond(string params) {
  int r = -1; // unknown
  double x, y, theta;

  if (getRobotPose(robotname,x,y,theta)) {
    if ((fabs(x - 2) <= 4) && (fabs(y - 2) <= 4)) {
        // cerr << "\033[22;34;1mCloseToHome\033[0m" << endl;
        r = 1;
    }
    else {
        r = 0;
    }
  }
  return r;
}
