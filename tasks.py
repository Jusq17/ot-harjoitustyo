from invoke import task

@task
def start(ctx):
    ctx.run("python src/index.py", pty=False)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)