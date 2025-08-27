def announce(f):
    def wrapper():
        print("about to run the function")
        f()
        print("am done with the function")
    return wrapper
@announce
def hello():
    print("hello world")
hello()

def logging(loggedin):
    def wrapper1():
        print("About to log in")
        loggedin()
        print("Am now logged in")
    return wrapper1
@logging
def dashboard():
    print("This is the dashboard")
dashboard()