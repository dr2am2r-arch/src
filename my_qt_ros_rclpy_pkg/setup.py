from setuptools import find_packages, setup

package_name = 'my_qt_ros_rclpy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='daewon',
    maintainer_email='daewon@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'msg_pub_qt = my_qt_ros_rclpy_pkg.msg_pub_qt:main',
        'msg_sub_qt = my_qt_ros_rclpy_pkg.msg_sub_qt:main',
        ],
    },
)
