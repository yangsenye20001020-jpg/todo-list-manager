from app import add_task, list_tasks, remove_task, tasks

def test_add_task():
    tasks.clear()
    add_task("Test 1")
    assert tasks == ["Test 1"]

def test_remove_task():
    tasks.clear()
    add_task("Test 1")
    remove_task(0)
    assert tasks == []
