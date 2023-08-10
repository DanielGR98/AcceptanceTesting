from behave import given, when, then
from todo_list import TodoListManager

@given('the to-do list is empty')
def step_impl(context):
    context.manager = TodoListManager()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.manager.add_task(task)
    context.added_task = task

@then('the to-do list should contain "{task}"')
def step_impl(context,task):
    tasks = context.manager.list_tasks()
    assert context.added_task in tasks

###############################################

@given('the to-do list contains tasks')
def step_impl(context):
    context.manager = TodoListManager()
    context.manager.add_task('Tasks: ')
    for row in context.table:
        context.manager.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.task_list = context.manager.list_tasks()

@then('the output should contain')
def step_impl(context):
    
    expected_output_lines = [line.strip() for line in context.text.strip().split('\n')]
    actual_output_lines = [line.strip() for line in context.task_list]
    
    assert expected_output_lines == actual_output_lines, f"Expected: {expected_output_lines}, Actual: {actual_output_lines}"

###############################################

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.manager.mark_task_completed(task)

@then('the to-do list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    tasks = context.manager.tasks
    assert any(task.title == task_name and task.status == "Completed" for task in tasks)

###############################################

@when('the user clears the to-do list')
def step_impl(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.manager.tasks) == 0