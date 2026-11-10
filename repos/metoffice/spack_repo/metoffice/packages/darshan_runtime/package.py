from spack_repo.builtin.packages.darshan_runtime.package import DarshanRuntime as DarshanRuntimeBase

from spack.package import *

class DarshanRuntime(DarshanRuntimeBase):
    """
    Set the runtime environment for the darshan tool on EPCC systems.
    """
    
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        
        env.set("SRUN_EXPORT_ENV", f"ALL,LD_PRELOAD={self.prefix.lib}/libdarshan.so")