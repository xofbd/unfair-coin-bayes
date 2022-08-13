from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, RadioField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class ProbabilityForm(FlaskForm):
    probability = FloatField('Probability (0 to 1):',
                             render_kw={'placeholder': 0.5},
                             validators=[InputRequired(), NumberRange(min=0, max=1)])
    prior = RadioField('Choose Prior',
                       default='Uniform',
                       choices=['Uniform', 'Beta'],)
    param_a = IntegerField('a',
                           default=1,
                           render_kw={'placeholder': 2},
                           validators=[InputRequired(), NumberRange(min=0)])
    param_b = IntegerField('b',
                           default=1,
                           render_kw={'placeholder': 2},
                           validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')
