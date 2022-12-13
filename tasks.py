from invoke import task

@task
def start(ctx):
    ctx.run("python src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests/logictest.py", pty=False)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests/logictest.py", pty=False)
