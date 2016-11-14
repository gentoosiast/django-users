# Add 'autofixture' to INSTALLED_APPS in ask/settings.py
# ./manage.py shell
# execfile('/home/box/autofixture.py')

from autofixture import AutoFixture
from qa.models import Answer

fixture = AutoFixture(Answer, generate_fk=True)
entries = fixture.create(57)
