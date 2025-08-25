Check R and Rstudio
-------------------

Launch Rstudio, and in the Console (left window), type::
```r
example(density)
```

This should display a series of graphics (Press `Enter` to advance). Close RStudio.
	      
Check Git
---------

Download the course materials using Git by entering the following command line in a Terminal:: 

    git clone https://github.com/barburevencu/PPE

You should see a message ``Cloning into 'PPE'...`` and, if everything goes well, all the currently available
course materials (python scripts, data files, ...) should be downloaded in a new subdirectory called ``PPE``, within the current working directory. You can cd into it and list its content:

```bash
cd PPE # Changes the current working directory to the PPE folder
pwd # Displays the address of the current working directory
ls # Lists the contents of the current working directory
```

Your Terminal window should more or less look like this:

![alt text](<./Images/git.png>)
![Git screenshot](./Images/git.png)

**Warning**
   If a folder named ``PPE`` already exists in the current working
   directory, git will stop and will not download the content of the remote PPE
   repository. In that case, you must delete or move the existing ``PPE`` folder
   before running the ``git clone`` command above.

   When you open a Terminal, the current working directory is your Home/User
   directory, until you start navigating the file system with the `cd`
   (change directory) command.

Check Python
------------

Assuming you are in the PPE directory, navigate to the Test folder, then run the following python script and play the game in the Terminal.

```bash
cd Installation/Test
python python-basic-test.py
```

Check basic graphics
--------------------
Make sure (for instance, by using `pwd`) that you are still in the ```PPE/Installation/Test``` directory. Then, type:

```bash
python python-graphics-test.py
```
![alt text](Images/koch.png)

To check the code, launch the Visual Code editor and open the python file ``PPE/Installation/Test/koch.py``. 

Check pygame
------------
[Pygame](https://www.pygame.org/news) is a Python library to create simple audio visual games. 

While still in the ```PPE/Installation/Test``` directory, launch the python script `pygame-test.py`.
![alt text](Images/hering.png)

Check Expyriment
----------------
[Expyriment](https://expyriment.org) is a Python library for designing and conducting behavioural and neuroimaging experiments.

While still in the ```PPE/Installation/Test``` directory, launch the python script `expyriment-test.py`.

   cd ~/PCBS/experiments/xpy_parity_decision
   python parity_feedback.py

This should run a short experiment where participants must check whether a number is odd or even.

Keep your local copy of the course material up to date
------------------------------------------------------

The course materials are often updated. To make sure you have the latest version, you can synchronize your local copy with the github repository http://github.com/chrplr/PCBS, with the commands:

.. code-block:: bash

      cd ~/PCBS
      git pull

Notes:

- if the PCBS directory is not in your home directory (``-``), you will need to use the appropriate path in the first cd command.
- do not manually modify or create new files in the ``PCBS`` folder.
  If you do so, git will notice it and might prevent an automatic upgrade
  and ask you to ‘resolve conflicts’. If you get such a message, the
  simplest course of action, for beginners, is to delete the PCBS folder (or
  move it if you wnat to keep a copy of your modifications) and reissue the
  ``git clone`` command above to reload the full folder.