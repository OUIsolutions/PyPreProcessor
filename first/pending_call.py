from build_in_procedure import BuildInProcedure

class PendingCall:

    def __init__(self,procedure:BuildInProcedure) -> None:
        self.procedure= procedure
        self.args = []
        