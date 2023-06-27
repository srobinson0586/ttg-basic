import copy

class TestSection:
    def __init__(self, name):
        self.name = name
        self.funcs = []

    def add(self, func):
        self.funcs.append(func)

    def run(self, run_all = False):
        print("Running all {} tests . . .".format(self.name))
        
        success = True
        for f in self.funcs:
            if not f.run(run_all = False, verbose = True):
                success = False
                if not run_all:
                    break

        if success:
            self.print_success()
        else:
            self.print_failure()

        return success

    def print_success(self):
        print("All {} tests passed!\n".format(self.name))

    def print_failure(self):
        print("\nAt least one {} test failed :(\n".format(self.name))


class TestFunc:
    def __init__(self, func, copy_input = False):
        self.func = func
        self.cases = []
        self.copy_input = copy_input

    def add(self, args, output):
        case = TestCase(self.func, args, output, self.copy_input)
        self.cases.append(case)

    def run(self, run_all = False, verbose = False):
        success = True
        for case in self.cases:
            if not case.check():
                success = False
                if not run_all:
                    break

        if success and verbose:
            self.print_success()
            
        return success

    def print_success(self):
        print("  {} passed!".format(self.func.__name__))

    def print_failure(self):
        print("  {} failed".format(self.func.__name__))


class TestCase:
    def __init__(self, func, args, output, copy_input):
        self.func = func

        ### Automatically convert a single non-tuple argument into a singleton.
        if isinstance(args, tuple):
            self.args = args
        else:
            self.args = (args, )
            
        self.output = output
        self.copy_input = copy_input

    def check(self):
        if self.copy_input:
            inputs = copy.deepcopy(self.args)
        else:
            inputs = self.args
            
        actual = self.func(*inputs)
        
        if actual == self.output:
            rtn = True
        else:
            self.print_failure(actual)
            rtn = False

        return rtn

    def print_failure(self, actual):
        template = "  fail: {}{} should be '{}', but returned '{}'"
        if len(self.args) == 1:
            arg_str = "({})".format(self.args[0])
        else:
            arg_str = str(self.args)
            
        msg = template.format(self.func.__name__, arg_str, self.output, actual)
        print(msg)
