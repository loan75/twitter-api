# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields, reqparse
from app.db import tweet_repository
from app.models import Tweet

api = Namespace('tweets')

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.String
})

message_parser = reqparse.RequestParser()
message_parser.add_argument('message', type=str, help='New message')


@api.route('/')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):

    @api.marshal_with(tweet)
    def get(self):
        return tweet_repository.tweets

    @api.expect(message_parser)
    @api.marshal_with(tweet)
    def post(self):
        new_value = message_parser.parse_args()['message']
        result = tweet_repository.add(Tweet(new_value))
        if result is None:
            api.abort(404)
        else:
            return result, 201


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):

    @api.marshal_with(tweet)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet

    @api.marshal_with(tweet)
    def delete(self, id):
        is_deleted = tweet_repository.delete(id)
        if is_deleted:
            return {}, 204
        else:
            api.abort(404)

    @api.expect(message_parser)
    @api.marshal_with(tweet)
    def put(self, id):
        new_value = message_parser.parse_args()['message']
        result = tweet_repository.update(id, new_value)
        if result is None:
            api.abort(404)
        else:
            return result, 201
