# Control Panel

This piece of software aims to recreate a control panel from a fictional spacecraft. It takes part in a escape room as the last test to pass. 

## Usage
The user is meant to get find out the password to login to the spacecraft Control Panel. And once inside, find the way to shut down the system.

## Developer notes
First of all, set up the virutual environment with all the necessary packages.
```
pipenv install --dev
```

To run the program in the developement environment simply run:
```
pipenv run python __main__.py
```

## Generate the executable

To generate the executable file run the `build_dist.sh`, located in the `scripts` folder,  in a unix based terminal and the `dist` folder should be generated after the script finishes.
```
./build_dist.sh
```

>  **Note:** Tested in windows 10 and macOS Catalina.

After the scirpt is done the distributable file will be abailable in the `scripts/Output` folder as a **zip** file; `Control Panel.zip`.
