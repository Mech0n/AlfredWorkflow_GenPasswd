# AlfredWorkflow_GenPasswd
>  Use  alfred generate passwd

[![e513d071b0f138abbcb4ae679656bded.png](https://img.vaala.cloud/images/2021/01/26/e513d071b0f138abbcb4ae679656bded.png)](https://img.vaala.cloud/image/YFQg)

#### Installing

Download [**GenerationPasswd.alfredworkflow**](https://github.com/Mech0n/AlfredWorkflow_GenPasswd/raw/main/GenerationPasswd.alfredworkflow)

And we need:

- [Alfred](https://www.alfredapp.com/)
- `/usr/bin/python -m pip  install python2-secrets --user`

#### Other Questions

- Q1: `/usr/bin/python: No module named pip` when `/usr/bin/python -m pip  install python2-secrets --user`:

  Your macOS system version of python does not have pip, do this to install pip :

  ```shell
  curl https://bootstrap.pypa.io/2.6/get-pip.py -o get-pip.py
  /usr/bin/python get-pip.py --user
  ```

  Or you can change the workflow, because the workflow use `/bin/zsh`, you can change the command.

  ![897de8f669d1f70ab39b781356b48a12.png](https://img.vaala.cloud/images/2021/01/26/897de8f669d1f70ab39b781356b48a12.png)

⚠️Warning: Due to some dependency issues, my script only supports python2. A script that supports python3 is coming soon.

