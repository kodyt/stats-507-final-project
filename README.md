# stats-507-final-project
AI-Powered Code Tutoring Tool

# Deployed App
Navigate to [this link to visit the deployed project](https://aicodingtutor.vercel.app/) (https://aicodingtutor.vercel.app/)

For the report on this project, [Click here](./STATS_507_Final_Project.pdf).

# Run the model only
The executable file, run_backend_example.sh can be ran to run an example of how the model works. This script creates a virtual environment, pip installs the requirements.txt, and then runs the example python script located in the backend folder, saves the output of the two examples in output.txt in the backend folder. 

**NOTE:** The model needs time to warm up, so the first run of the project may take up to 20 seconds.
```
# IF NEEDED, make the script executable
$ chmod +x run_backend_example.sh

# Run the script
$ ./run_backend_example.sh

```

# Run the project locally
Run the backend and frontend servers in different terminals.
```
# Backend
$ cd backend

# Create a virtual environment for packages.
# Refer to the documents on how to do so: https://docs.python.org/3/library/venv.html
$ pip install -r requirements.txt
$ python3 app.py

# Frontend
$ cd frontend
$ npm run dev
```