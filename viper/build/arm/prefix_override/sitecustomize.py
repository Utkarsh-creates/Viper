import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/utkarsh/ROS2_Workspace/Viper/Viper/install/arm'
