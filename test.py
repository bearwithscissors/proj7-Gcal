import flask
import arrow

import CONFIG


from flask_main import interpret_time

def test():
    '''
    test interpret_time
    '''
    begin_time = interpret_time("10am")
    end_time = interpret_time("11pm")

    assert(begin_time == "2016-01-01T10:00:00-08:00")
    assert(end_time == "2016-01-01T23:00:00-08:00")

test()
