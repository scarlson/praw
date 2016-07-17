from praw.models import Subreddit
import mock

from ... import IntegrationTest


class TestMultireddit(IntegrationTest):
    @mock.patch('time.sleep', return_value=None)
    def test_add(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette('TestMulireddit.test_add'):
            multi = self.reddit.user.multireddits()[0]
            multi.add('redditdev')
            assert 'redditdev' in multi.subreddits

    @mock.patch('time.sleep', return_value=None)
    def test_delete(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette('TestMulireddit.test_delete'):
            multi = self.reddit.user.multireddits()[0]
            multi.delete()

    @mock.patch('time.sleep', return_value=None)
    def test_remove(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette('TestMulireddit.test_remove'):
            multi = self.reddit.user.multireddits()[0]
            multi.remove('redditdev')
            assert 'redditdev' not in multi.subreddits

    @mock.patch('time.sleep', return_value=None)
    def test_rename(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette('TestMulireddit.test_rename'):
            multi = self.reddit.user.multireddits()[0]
            multi.rename('PRAW Renamed')
            assert multi.display_name == 'PRAW Renamed'
            assert multi.name == 'praw_renamed'

    def test_subreddits(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMulireddit.test_subreddits'):
            assert multi.subreddits
        assert all(isinstance(x, Subreddit) for x in multi.subreddits)


class TestMultiredditListings(IntegrationTest):
    def test_comments(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette(
                'TestMuliredditListings.test_comments'):
            comments = list(multi.comments())
        assert len(comments) == 100

    def test_controversial(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette(
                'TestMuliredditListings.test_controversial'):
            submissions = list(multi.controversial())
        assert len(submissions) == 100

    def test_gilded(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMuliredditListings.test_gilded'):
            submissions = list(multi.gilded())
        assert len(submissions) == 100

    def test_hot(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMuliredditListings.test_hot'):
            submissions = list(multi.hot())
        assert len(submissions) == 100

    def test_new(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMuliredditListings.test_new'):
            submissions = list(multi.new())
        assert len(submissions) == 100

    @mock.patch('time.sleep', return_value=None)
    def test_new__self_multi(self, _):
        self.reddit.read_only = False
        with self.recorder.use_cassette(
                'TestMuliredditListings.test_new__self_multi'):
            multi = self.reddit.user.multireddits()[0]
            submissions = list(multi.new())
        assert len(submissions) == 100

    def test_rising(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMuliredditListings.test_rising'):
            submissions = list(multi.rising())
        assert len(submissions) > 0

    def test_top(self):
        multi = self.reddit.multireddit('kjoneslol', 'sfwpornnetwork')
        with self.recorder.use_cassette('TestMuliredditListings.test_top'):
            submissions = list(multi.top())
        assert len(submissions) == 100
