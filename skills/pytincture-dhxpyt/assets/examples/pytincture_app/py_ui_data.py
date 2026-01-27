from pytincture.dataclass import backend_for_frontend, bff_policy

@backend_for_frontend
@bff_policy(roles={"analyst", "manager"})      # class-wide default (optional)
class py_ui_data:
    @bff_policy(roles={"manager"})             # stricter requirement for chat
    def dataset(self, *args, **kwargs):
        return open("dataset.json", "r").read()

    def reconciliation_dataset(self):
        return open("reconciliation.json", "r").read()