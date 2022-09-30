# QuaDigi_Task
 
<li>Task is solved using Visual Studio Code in Python 3.10.7</li>

<h3>Instructions to run the programing task code</h3>
<ol>
  <li>Be sure you have your Python IDE to interepret with Python 3.10.7 (it doesn't have to be Visual Studio Code)</li>
  <li>I always advice to use Python Virtual Environment on top of  core Python installation so, if any problems arise regarding to Python files and etc., they easily can be  managed without touching original python installation. This said, run the command on cloned or unzipped project location  "py -m venv vEnv3_10_7"</li>
    <li>run "pip install -r requirements.txt" at project location, So, we don't need to look 1 by 1 what to install for missing libraries (Be sure your vEnv3_10_7 is acting as Python interpreter but not the core python installation</li>
  <li><b>Clone RestAPI from the link:</b> (It could be part of same project but in most cases RestAPI should be seperate project with its own rules) https://github.com/purelog1c/QuaDigi-RESTApi-Program  </li>
    <li><b>Follow the instructions on QuaDigi-RESTApi-Program README.txt file.</b> to run API on local Server. The server is without WSGI module, so it should work on any OS without problem.</li>
     <li>Be sure that RestAPI is running to be able to use functionality of File upload on this project for HTTP requests</li> 
     <li>If all done until here, just <b>run the main.py</b> and follow the small pipeline program to test the workability of the provided task solution</li>
     <b>Some Notes:</b>
      <ol type="A">
      <li> All validations are not handled fully but partly so, trying to break type or unnoticed rules will work in most cases in prompt. So, apologizes for that :)</li>
      <li>I solved the task from my understanding point of view, there might be and probably will be major or minor differences compared to actual programming task</li>
      <li>Refactoring is really needed. I take the credits. </li>
      <li>Functional tests are made internally(personally) but I might of course have missed something.</li>
      <li> In real world situation with well-defined requirements as user stories with well defined AC(Acceptence criteria) and an agile team coducting SCRUM, I believe       I would think and structure my development strategy way better depending on technology, aim and objectives of the product to be delievered.</li>
      </ol> 
</ol> 

Hopefully solution will match with your expectatitons.
