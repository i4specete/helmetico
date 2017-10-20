from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager

tasks = [dict(name="Create AWS administrator group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="Admin Group",
                                                          managed_policy= "AdministratorAccess",
                                                          state="Present"  )))]

tasks = [dict(name="Create AWS billing group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="Billing Group",
                                                          managed_policy= "Billing",
                                                          state="Present"  )))]

tasks = [dict(name="Create AWS Database Administrator group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="DatabaseAdministrator Group",
                                                          managed_policy= "DatabaseAdministrator",
                                                          state="Present"  )))]

tasks = [dict(name="Create AWS DataScientist group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="DataScientist Group",
                                                          managed_policy= "DataScientist",
                                                          state="Present"  )))]



tasks = [dict(name="Create AWS Developer group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="Developer Group",
                                                          managed_policy= "PowerUserAccess",
                                                          state="Present"  )))]



tasks = [dict(name="Create AWS NetworkAdministrator group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="NetworkAdministrator Group",
                                                          managed_policy= "NetworkAdministrator",
                                                          state="Present"  )))]



tasks = [dict(name="Create AWS SystemAdministrator group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="SystemAdministrator Group",
                                                          managed_policy= "SystemAdministrator",
                                                          state="Present"  )))]

tasks = [dict(name="Create AWS SecurityAudit group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="SecurityAudit Group",
                                                          managed_policy= "SecurityAudit",
                                                          state="Present"  )))]

tasks = [dict(name="Create AWS Read Only group",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="ReadOnly Group",
                                                          managed_policy= "ViewOnlyAccess",
                                                          state="Present"  )))]

#USERS


tasks = [dict(name="Create User",action=dict(module="iam_group",
                                                      args=dict(
                                                          name="ReadOnly Group",
                                                          managed_policy= "ViewOnlyAccess",
                                                          state="Present"  )))]