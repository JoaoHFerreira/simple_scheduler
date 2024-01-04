1. Add unit tests for each new function (0 covered right now)
2. Add poetry as dependency manager;
3. Add logs for better understanding
    1. In this topic consider create a server to communicate between the task and the scheduler
4. Define run task as assync synce not have depencies;
5. Define a better way to schedule, right now all tasks runs in same time scheduler, add as parameter in config, and run task only if is in the right scheduler, understand how to right keep track of this.
6. As code grows, split into classes and modules, as necessary;
7. As the code grows add a database connection to save metadata
8. The right now is not like a DAG, it just triggers the program, create a a way to perform the DAG algorith