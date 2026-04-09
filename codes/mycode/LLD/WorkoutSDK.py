"""
-----------------------------------------------
Clarify business goals
Validate current architecture
Review domain modeling
Identify tight coupling
Suggest refactor
Discuss extensibility
Cover testing gaps
Discuss performance
Align back to business
-----------------------------------------------
requirement clarification, correctness, consistency, scale/performance , maintainability/understandable, testability, observability, logging


1.  clarify requirements
    who are the user
    SDK internal/public
    is this mobile first?
    what scale? 10k users

2.  Review requirement vs implementation
    missing features
    missing validations
    hardcoded logic


- Layered architecture  -
    - Presentation/Facade Layer (Frontend/UI)- Managers,controller
    - Application/Service layer  - Application specific logic, transformation and parsing so
    - Business/Domain layer - core business rules
    - Infra layer/data access     -- DB,  external APIs, and logging   - SqlAccountRepository classes
    Separation of Concerns and Inward Dependencies
- Dependency Injection
- Interfaces for extensibility

- God class, business logic coupled with UI logic, no separation of concerns,
- Violation of solid principles
- Exception handling.
- Dependency Injection

 “This works for now, but if we scale workouts to multiple types or introduce personalization, this design might become hard to maintain.”

"""


class Exercise:
    def __init__(self, name, duration, calories_per_minute):
        self.name = name
        self.duration = duration
        self.calories_per_minute = calories_per_minute


class Workout:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty  # "beginner" or "advanced"
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def total_duration(self):
        total = 0
        for e in self.exercises:
            total += e.duration
        return total

    def total_calories(self):
        total = 0
        for e in self.exercises:
            calories = (e.duration / 60) * e.calories_per_minute
            if self.difficulty == "beginner":  # hardcoding  Enum
                calories = calories * 0.9
            elif self.difficulty == "advanced":
                calories = calories * 1.2
            total += calories
        return total


class WorkoutManager:
    def __init__(self):
        self.workouts = []

    def create_workout(self, name, difficulty):
        workout = Workout(name, difficulty)
        self.workouts.append(workout)
        return workout

    def get_workout(self, name):
        for w in self.workouts:
            if w.name == name:
                return w
        return None


"""
Code Reviews - 
Hard coding on difficulty --> make it enum 
and strategy pattern --->          DifficultyStrategy 
                                    /               \
                        BeginnerStrategy(-10%)    AdvancedStrategy (+20%)
Workout class does too many things - calculating calories, duration  
        Exercise should calculate calories 
        Strategy should modify the calories 
        Workout should aggregate the calories 
Validations -> duration <0, difficulty INVALID, calories=0 Precision logic ->
WorkoutManager is Inmemory, workouts are lost if restart happens 
    Infra layer -->   IWorkoutRepository
                    /                   \
                  InMemoryRepository   SQLRepository 
Performance issue with get_workout  -- linear search O(n) no indexing. maps for InMemoryRepo
No Logging Metric collection  Async logging emitting metrics 

Not thread safe - concurrency issue
   
"""

'''
---------
VALIDATION Exception
private methods,variables
logging 
concurrency , 
provide comments for why not what, type -int,string

Versioning 
Feature flagging config
AI recommendations -++

'''


#----------------Workout session---------------#


'''
Allow users to start a workout session.

Track completed exercises.

Mark workout as completed when all exercises are done.

Calculate total calories burned during the session.

Support pausing and resuming a session.

Expose a way to get user progress percentage.
'''

import time


class WorkoutSession:
    def __init__(self, workout):
        self.workout = workout
        self.current_index = 0
        self.completed = False
        self.start_time = None
        self.paused = False
        self.total_calories = 0

    def start(self):
        self.start_time = time.time()

    def complete_exercise(self):
        if self.completed:
            return "Workout already completed"

        exercise = self.workout.exercises[self.current_index]   # domain modeling issue
        calories = (exercise.duration / 60) * exercise.calories_per_minute

        if self.workout.difficulty == "beginner":
            calories *= 0.9
        elif self.workout.difficulty == "advanced":
            calories *= 1.2

        self.total_calories += calories
        self.current_index += 1

        if self.current_index >= len(self.workout.exercises):
            self.completed = True

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def progress(self):
        return (self.current_index / len(self.workout.exercises)) * 100


"""
Business 
Is a session resumable on app restart? Should session persist to storage?
Is the calorie calculation is based on user or just difficulty?
should pause affect calorie calculation? 
user can skip the exercise?
who is the user - mobile only sdk 

domain modeling issue  self.workout.exercises accessing these 

difficulty magic strings used 
workout internal logic exposed calorie calculation 
state management problem --- complete_exercise() can be called before start()
STATE ---> NOT_STARTED, ACTIVE, PAUSED, COMPLETED and enforce the transitions 
Pause should stop the timer, record elapsed time, adjust calories 
No behavioural impact-- just boolean flag 
division by zero in progress --- 
client can retry complete call --> leading to inconsistent state -> need idempotency, 
no persistent layer -> repository abstraction  

"""


#----------------GoalTracker session---------------#







