import cmd
import os
import sys
import subprocess
import json

class OShellCmd(cmd.Cmd):
    def __init__(self):
        super().__init__(completekey='tab')
        self.prompt = "> "
        self.output = b''
        self.aliases = {}

    def parseline(self, line):
        if '|' in line:
            return 'pipe', line.split('|'), line
        return super().parseline(line)

    def postcmd(self, stop, line):
        if self.output:
            print(json.loads(self.output.decode("utf-8")))

    def do_pipe(self, args):
        for arg in args:
            self.onecmd(arg)

    def do_help(self, args):
        for item in dir(self):
            if item.startswith("do_") and item not in ("do_help", "do_pipe"):
                print(item[3:])

class OShell():
    schemas = {}
    schemas_dir = "Schemas"
    commands = {}
    commands_dir = "Commands"
    rules = {}
    rules_dir = "Rules"
    alias = {}

    def __init__(self):
        pass

    def run(self, args):
        self.load_schemas()
        self.load_commands()
        self.load_rules()

        self.cmd = OShellCmd()
        self.cmd.cmdloop()

    def load_schemas(self):
        for schema in os.listdir(self.schemas_dir):
            self.schemas[schema.split(".")[0]] = schema.split(".")[0]

    def load_commands(self):
        for command_file in os.listdir(self.commands_dir):
            command_name = command_file.split(".")[0]
            self.commands[command_name] = command_name
            setattr(OShellCmd, "do_" + command_name, self.gen_command(command_name))

    def gen_command(self, command_name):
        return lambda s, args: self.run_command(command_name, args)

    def load_rules(self):
        pass

    def run_command(self, name, args):
        cmd = [os.path.join(self.commands_dir, name)]
        cmd.append(args)
        self.cmd.output = subprocess.Popen(cmd,
                                           stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(
            input=self.cmd.output)[0]


OShell().run(sys.argv)
