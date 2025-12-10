from setuptools import find_packages, setup

package_name = 'simple_py_pkg'

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
    maintainer='berkay',
    maintainer_email='berkay@todo.todo',
    description='Basit bir ROS 2 Python publisher örneği',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'py_node = simple_py_pkg.simple_py_node:main',
            'counter_node = simple_py_pkg.template_node:main',  # 👈 Eğer dosyan template_node.py ise
            'talker = simple_py_pkg.talker:main',
        ],
    },
)
