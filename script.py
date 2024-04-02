from job_templates.models import ProjectJobTemplates
import logging
LOGGER = logging.getLogger('django')
def fixing_job_templates():
    steps= [ 
        {
                "order": 0,
                "step_name": "pre hook",
                "is_conditional_step": False,
                "step_code": "PRE_HOOKS",
                "environment_variables": None
                },
        {
                "order": 1,
                "step_code": "DEPLOYMENT_MANIFEST_CREATOR",
                "step_name": "Deployment Manifest Creator",
                "is_conditional_step": False,
                "environment_variables": None
            }, {
                "order": 2,
                "step_code": "K8S_DEPLOYMENT_MANIFEST_APPLY",
                "step_name": "K8s deployment manifest apply",
                "is_conditional_step": False,
                "environment_variables": None
            },
            {
                "order": 3,
                "step_name": "post hook",
                "is_conditional_step": False,
                "step_code": "POST_HOOKS",
                "environment_variables": None
                }]
    steps_old = [{'order': 0, 'step_code': 'K8S_MANIFEST_APPLY', 
                  'step_name': 'k8 deploy', 
                  'is_conditional_step': False
                  , 'environment_variables': None}]
    objects=ProjectJobTemplates.objects.all()
    for obj in objects:
        # i.job_template=default_v2_template
        for jobs in obj.job_template['jobs']:
            if jobs['job_code']=='deploy_job':
                print(jobs["steps"])
                if jobs["steps"] == steps_old:
                    jobs["steps"] = steps
                # jobs.pop('steps')
                # jobs['steps']=steps
        obj.save()
fixing_job_templates()
