from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, RadioField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class ProbabilityForm(FlaskForm):
    probability = FloatField(
        "Probability of heads",
        render_kw={"placeholder": 0.5},
        validators=[InputRequired(), NumberRange(min=0, max=1)]
    )
    prior = RadioField(
        "Choose Prior",
        default="Uniform",
        choices=["Uniform", "Beta"]
    )
    param_a = IntegerField(
        "Shape parameter α",
        default=1,
        render_kw={"placeholder": 2},
        validators=[InputRequired(), NumberRange(min=0)]
    )
    param_b = IntegerField(
        "Shape parameter β",
        default=1,
        render_kw={"placeholder": 2},
        validators=[InputRequired(), NumberRange(min=0)]
    )
    submit = SubmitField("Submit")
