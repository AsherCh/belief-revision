# Belief revision Assignment
This is an implementation of a belief revision agent. 

## How to run

1. Navigate to the game directory.
   ```bash
      cd belief-revision
2. Execute main.py file to run the game
    ```bash
      python main.py
3. Follow the instructions displayed on the screen to interact with the agent. 

## Dependencies
This project requires Python3. Please ensure that pyhton3 is installed in the system. In addition, sympy is needed to run the agent. To install sympy, run the following command:
```bash
pip install sympy
```

## Files

- `main.py`: Entry point for the belief revision agent. Run this file to interact with the agent.
- `validator.py`: Validates the user's input in the terminal. 
- `expansion.py`: Handles the expansion of belief base. 
- `contraction.py`: Handles the contraction of belief base. 
- `entailment.py`: Handles entailment of belief base with a given sentence.
- `belief_base.py`: Stores the belief base and provides methods to manipulate it.
- `AGM_postulate_consistency.py`: Implements the AGM postulate of consistency.
- `AGM_postulate_contraction.py`: Implements the AGM postulates of contraction.
- `AGM_postulate_expansion.py`: Implements the AGM postulates of expansion.

## Credits
This belief revision agent has been implemented by Group 39 as an assignment for the course Introduction to AI 02180. 