
# Requires Changes
### 1 specification requires changes

This is hands down one of the best visualization projects I've ever reviewed, well done! There is only one minor bug that needs to be corrected, but overall you have done an excellent work here. After you have corrected this bug, the next step is to host this project so you may include this as a part of your portfolios. The simplest is to host it in bl.ocks.org, but if you prefer to have more freedom e.g. access to server-side computing, hosting companies like Heroku allows you to host there for free, or you can also try IBM bluemix, Amazon AWS, or Google App Engine.

*Thank you so much for your kind words! I really went applied myself here hoping for it to be a good addition to my portfolio, I'm glad you think it is! Let's hope my future interviewers think the same.*

*I actually tried to use bl.ocks.org, but due to the size of the data file (4 MB, exceeds the 1 MB limit), I can't. So, I'll host it using one of those services, thanks for the tip! And with server-side computing, I can use python and/or SQL to dynamically create more complex queries for my next projects. I'm not sure how to do it yet, but I think this is something really useful to learn next.*

## Code Structure and Functionality

### The visualization renders and any interactions or animations work as the reader interacts with the visualization.
*ok*

### Large code chunks are commented and all complex code is adequately explained with comments. Comments are not overused to explain obvious code.

The code is properly commented, good work. You can improve the commenting further by implementing documentation tools for javascript such as JsDoc, with which you can add more information to the functions you have created. I found that to be useful to document the functions I have created for when I need to revisit them much later. One feature from JsDoc is its capability to generate documentation in form of html documents automatically from the comments you've written.

*I've read a bit about JsDoc, and will implement it here when I've got the time, and to all my next projects! Thanks for the tip.*

### The code uses formatting techniques in a consistent and effective manner to improve code readability.

The code is well-formatted, good job.

(Optional) "use strict"; directive needs to be applied to the entire script and not just a function. To ensure it is the case, I suggest moving this directive to the top of the script right under \<script> tag.

*Done, moved "use strict" outside the function.*

## Visualization is Explanatory

### The visualization centers on a specific, clear finding in the data.

Excellent work here! You have used advanced visualization techniques to present your findings from the data. The visualization is pleasant to read and interact with. Well done crafting a very good project.

*Thank you!*

### (Requires Change) The selected finding is clearly communicated. Design choices foster communication between the reader and the visualization.

Again, you have done a superb work here. There is only one small bug that I noticed: Pressing the "Start Animation" a few times would cause multiple dialog boxes to appear.

(Optional) In addition to the "Quit" button inside the dialog bar, replacing "Start Animation" button with "Stop Animation" when the animation is running might be a good idea to handle the issue above.

*Created a function called aniBtnControl that handles the behavior of the #animation-btn button. Now, it remains disabled unless there's an animation running. If that is the case, the user can use the button to pause and resume the animation as he/she sees fit. Used jQuery to enable/disable the button as I didn't find any way to do it in D3.*

## Design

### A reader’s summary of the graphic would closely match the written summary in the README.md file, or a reader would identify at least 1 main point or relationship that the graphic attempts to convey.

The Summary section summarizes the findings quite well, although I suggest including more details there i.e. what findings, specifically, should readers expect to find by reading the visualization?

*Reviewed the Summary section to include a few of the guided findings, and to explain the objectives behind the animation.*

### The visualization includes interaction or animation. The interaction or animation may be simple, such as a hover, tooltip, or transition. Interaction or animation enhances understanding of the data.

*ok*

### Initial design decisions such as chart type, visual encodings, layout, legends, or hierarchy are included at the beginning of the Design section in the README.md file.

All design decisions have been explained in great detail, excellent work!

*Thanks*

## Feedback and Iteration

### Feedback has been collected from at least three people throughout the process of creating the data visualization. The feedback is documented in the Feedback section of the README.md file.

*ok*

### The project includes evidence that the visualization has been improved since the first sketch or the first coded version of the visualization. All of the feedback is listed in the Feedback section of the README.md file. Most design choices and changes are accounted for in the Design section of the README.md file. If no changes were made to the visualization after gathering feedback, this decision is explained.

*ok*
