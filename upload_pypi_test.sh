#!/bin/zsh

rm -rf ./build
rm -rf ./dist
rm -rf ./yourtools.egg-info

pip3 uninstall yourtools

python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*