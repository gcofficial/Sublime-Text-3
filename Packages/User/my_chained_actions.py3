import sublime, sublime_plugin

class MyChainedActionsCommand():
    def run(self, edit):
        self.view.run_command("reveal_in_side_bar")
        self.view.run_command("focus_side_bar")
