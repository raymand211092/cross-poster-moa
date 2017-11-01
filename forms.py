from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField
from wtforms.validators import DataRequired, Email


class SettingsForm(FlaskForm):
    enabled = BooleanField('Enable Bridge?')

    post_to_twitter = BooleanField('Post to Twitter?')
    split_twitter_messages = BooleanField('Split messages on Twitter?')

    post_to_mastodon = BooleanField('Post to Mastodon?')
    toot_visibility = SelectField('Toot visibility',
                                  choices=[
                                      ('public', 'Public'),
                                      ('private', "Private"),
                                      ('unlisted', 'Unlisted'),
                                  ])


class MastodonIDForm(FlaskForm):
    mastodon_id = StringField('Enter your Mastodon ID', validators=[DataRequired(), Email()])
