# Algorithms and Data Structures (ADS)

Welcome to the repository dedicated to learning Algorithms and Data Structures (ADS). 


<p align="center">
  <img src="./static/logo.png" alt="OS logo" width="10%" height="auto">
</p>

The main topics are algorithms and data structures.


### Basic concepts

- ``Algorithms``: is a step-by-step procedure or set of rules for solving a specific problem. It takes an input, processes it, and produces an output. Algorithms can be simple (like adding two numbers) or complex (like sorting or searching large datasets).
- ``Data Structures``: is a way to store and organize data efficiently. It defines how data is arranged, accessed, and manipulated in memory. Examples include lists, stacks, queues, trees, and graphs.

- Algorithms Operate on Data Structures: Algorithms process, search, sort, or modify data stored in data structures.
- Efficiency Depends on Data Structure: The choice of data structure affects algorithm performance. (e.g., Searching in a list is O(n), but in a dictionary it’s O(1)).
- Optimizing Algorithms Requires the Right Data Structure: For example, Dijkstra’s shortest path algorithm is efficient when used with a priority queue.

Idea: 
- *Algorithms* are the **recipes** for solving problems.
- *Data structures* are the **ingredients** used in these recipes.

### Repository Structure:

- Theory [docs](./docs)
- Exercices [Problems](./problems/)



### How to Use This Repository:

- Navigate to each main topic directory to find scripts and explanations for that specific concept.
- Use the scripts as practical examples to reinforce theoretical knowledge.
- Refer to the detailed explanations for a deeper understanding of each concept.

Feel free to explore, learn, and contribute to this repository. If you have any questions or need clarification on any topic, don't hesitate to reach out. Happy learning!

## Collaborative Course Repository Guide

This repository also is used for our collaborative work and assignments for the course. This document provides a step-by-step guide on how to interact with the repository efficiently.

### Getting Started

1. **Fork the Main Repository:**
   - Fork the main repository into your GitHub account. This action creates a new repository in your account, and you'll be working from there.

2. **Sync Your Repository:**
   - If you've forked the repository earlier, it's essential to keep it up to date. Follow these steps to sync your fork with the latest version:
     - Configure the remote for your fork:
       ```bash
       git remote add upstream https://github.com/Alvaro8gb/ADS
       ```
     - Fetch any changes to the upstream:
       ```bash
       git fetch upstream
       ```
     - Checkout the local master branch of your fork:
       ```bash
       git checkout main
       ```
     - Merge changes from the upstream into your master branch:
       ```bash
       git merge upstream/main
       ```

### Making Changes

3. **Work on Assignments:**
   - Make any necessary changes to your repository according to the specific assignment.

4. **Commit and Push:**
   - Commit your changes to your local repository:
     ```bash
     git commit -m "Your descriptive commit message"
     ```
   - Push your changes to your online repository:
     ```bash
     git push origin main
     ```

5. **Create a Pull Request:**
   - Submit a pull request so that we can review your changes and merge them into the main repository.
   - If everything is satisfactory, your changes will be incorporated into the main repository. If not, you'll receive feedback on why.

### Note:
- The fork and sync process is typically done only once during the course, ensuring that you are working with the latest version of the main repository.
- Follow these guidelines to maintain a clean and organized collaborative environment. If you encounter any issues or have questions, feel free to reach out for assistance.
- Each student has an individual folder dedicated to their assignments, providing an exclusive space for uploading their scripts.


## Evaluation
### Standard 
The code of the exercises is going to be evalauted considering this standard:

1. Readability and Maintainability (1-5):
- Check if the code is well-commented and has clear, descriptive variable and function names.
- Assess the overall structure and organization of the code. Is it easy to follow?
- Look for code duplication and assess whether the code follows the DRY (Don't Repeat Yourself) principle.

2. Correctness (1-5):
- Review the code for logical errors and ensure it produces the expected output.
- Check if the code handles edge cases and error conditions appropriately.
- Verify that the code adheres to the specified requirements or design specifications.

### Scale 

**5: Excellent**

- Code is well-organized, highly readable, and maintainable.
- Adheres to coding standards and follows best practices.

**4: Good**

- Code is generally well-organized and readable.
- Adheres to coding standards but may have a few minor deviations.

**3: Average**

- Code is somewhat organized and readable, but improvements could be made.
- Adheres to some coding standards but may have notable deviations.

**2: Below Average**

- Code organization and readability need significant improvements.
- Deviations from coding standards are significant.

**1: Poor**

- Code organization and readability are severely lacking.
- Major deviations from coding standards.

### Mark 

$$ Mark = Readbility\_Maintainability * 0.2 +  Correctness * 0.8 $$
$$  1 <= Mark <= 5 $$

