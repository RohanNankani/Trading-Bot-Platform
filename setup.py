from setuptools import setup, find_packages

setup(
	name='tradingbot',
	version='0.1',
	packages=find_packages(),
	install_requires=[
		'click',
	],
	entry_points={
		'console_scripts': [
			'trade=cli:trade',
		],
	},
)