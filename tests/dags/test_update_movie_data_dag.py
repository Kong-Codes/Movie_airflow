import pytest
from airflow.models import DagBag


@pytest.fixture(scope='module')
def dagbag():
    return DagBag()


def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id='update_movie_data_dag')
    assert dag is not None
    # assert len(dag.tasks) == 3


def test_task_dependencies(dagbag):
    dag = dagbag.get_dag(dag_id='update_movie_data_dag')
    tasks = dag.task_dict

    assert sorted([task.task_id for task in dag.tasks]) == ['extract', 'initialize', 'update_values']

    assert tasks['initialize'].downstream_task_ids == {'extract'}
    assert tasks['extract'].downstream_task_ids == {'update_values'}


def test_initialize_task(dagbag):
    dag = dagbag.get_dag(dag_id='update_movie_data_dag')
    task = dag.get_task(task_id='initialize')
    assert task.task_id == 'initialize'


def test_extract_task(dagbag):
    dag = dagbag.get_dag(dag_id='update_movie_data_dag')
    task = dag.get_task(task_id='extract')
    assert task.task_id == 'extract'


def test_update_values_task(dagbag):
    dag = dagbag.get_dag(dag_id='update_movie_data_dag')
    task = dag.get_task(task_id='update_values')
    assert task.task_id == 'update_values'
