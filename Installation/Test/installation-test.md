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
cd PPE ### Changes the current working directory to the PPE folder
pwd ### Displays the address of the current working directory
ls ### Lists the contents of the current working directory
```

Your Terminal window should more or less look like this:

![alt text](<Screenshot 2025-08-25 at 14.41.17.png>)

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
cd Test
python human-guess-a-number.py
```

To go back one directory up the hierarchy, type `cd ..` in the Terminal.

Check basic graphics
--------------------
Make sure (for instance, by using `pwd`) that you are in the ```PPE/Test``` directory. Then, type:

```bash
python koch.py
```
![alt text](image.png)

To check the code, launch the Visual Code editor and open the python file ``PPE/test/koch.py``. 

Check pygame
------------

`Pygame <http://www.pygame.org>`__ is a Python library to create simple audiovisual games. It was installed along with expyriment. If you had to create a Python virtual environment when you installed expyriment, you need to activate it::

  conda activate expyriment  # if you use conda
  pyenv activate expyriment  # if you use standard python with pyenv

You can then check if pygame is installed by starting ``python`` on a command line and typing ``import pygame`` a the ``>>>` prompt. A message ``Hello from the pygame community.`` should be displayed. 
    
.. code-block:: bash

   cd ~/PCBS/stimuli/visual-illusions/
   python kanizsa_triangle.py

.. image:: images/kani.png
    :width: 200

.. code-block:: bash

   python hering.py

.. image:: images/hering0.png
    :width: 400

.. code-block:: bash

   python extinction-rotated.py 

.. image:: images/exctinction.png

   python lilac_chaser_blurred.py


Check Expyriment
----------------

`Expyriment <http://expyriment.org>`__ is a Python library for designing and conducting behavioural and neuroimaging experiments. 

If you had to create a Python virtual environment when you installed expyriment, you need to activate it (unless it is already activated in your current Terminal)::

  conda activate expyriment  # if you use conda
  pyenv activate expyriment  # if you use standard python with pyenv

Try to run the following experiment (Note that the programs can be interrupted at any time by pressing the ``Esc`` key).
  

.. code-block:: bash

   cd ~/PCBS/experiments/xpy_parity_decision
   python parity_feedback.py

This should run a small exepriment where the participant must chech the parity (odd or even) of numbers.
   

That's all folks !


Appendices
----------


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
  ``git clone`` command above to reload the full folder.)


.. _survival:


Basic surviving skill: how to enter command lines in a Terminal
---------------------------------------------------------------

Watch the video at   https://www.youtube.com/watch?v=2yhcWvBt7ZE&t and try to perform the activities in it (the instructions also work for Mac or Linux: you just need to open a standard Terminal while in Windows you start 'Git Bash'). Note: the game scripts mentioned in the video are available at https://github.com/chrplr/PCBS/tree/master/games/games.zip


For the moment, you mostly need to know the following three commands:

-  ``ls``: list the content of the current working directory
-  ``pwd``: path of current working directory
-  ``cd``: change directory

Read about them in http://linuxcommand.sourceforge.net/lc3_lts0020.php

Here are some resources to learn more about how to control your computer from a terminal:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom : https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange


.. rubric:: Footnotes

.. [1]  Read https://linuxhint.com/path_in_bash/ , locate the folder containing ``subl``,  then use a text editor to add the following line at the end of the file ``~/.bashrc``::

       export PATH="path_to_the_directory_containing_subl":"${PATH}"

   Once this is done, type `. ~/.bashrc` and enter the command ``subl``