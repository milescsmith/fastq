import nox

package = "fastq"
python_versions = ["3.10", "3.9", "3.8", "3.7"]
nox.options.sessions = (
    "black",
    "run_tests",
)
nox.needs_version = ">= 2023.4.22"

locations = (
    "src",
    "tests",
)

@nox.session(name="run_tests", python=python_versions)
def run_tests(session):
    session.install(".", "pytest", "coverage[toml]",)
    session.run("pytest", "-v", "tests")

@nox.session(name="black", python=["3.10"])
def black(session):
    session.install("black")
    args = session.posargs or locations
    session.install("black[jupyter]")
    session.run("black", *args)