##  GET all local packages
	python -m pip freeze --local > package.txt	
		OR
	pip freeze --local > package.txt	


## Install package from file
	python -m pip install -r package.txt
		OR
	pip install -r package.txt


## Activate env
	source Scripts/activate

## Deactivate env
	deactivate

## RUN
	python test.py