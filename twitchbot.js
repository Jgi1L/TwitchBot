
$(function() {
    var conn = null;

    function log(msg) {
        var control = $('#log');
        control.html(control.html() + msg + '<br/>');
        control.scrollTop(control.scrollTop() + 1000);
    }

    function connect() {
        disconnect();
        var wsUri = (window.location.protocol=='https:'&&'wss://'||'ws://')+window.location.host;
        conn = new WebSocket(wsUri);
        log('Connecting...');
        conn.onopen = function() {
            log('Connected.');
            update_ui();
        };
        conn.onmessage = function(e) {
            log('Received: ' + e.data);
        };
        conn.onclose = function() {
            log('Disconnected.');
            conn = null;
            update_ui();
        };
    }

    function disconnect() {
        if (conn != null) {
            log('Disconnecting...');
            conn.close();
            conn = null;
            update_ui();
        }
    }

    function update_ui() {
        var msg = '';
        if (conn == null) {
            $('#status').text('disconnected');
            $('#connect').html('Connect');
        } else {
            $('#status').text('connected (' + conn.protocol + ')');
            $('#connect').html('Disconnect');
        }
    }

    $('#connect').click(function() {
        if (conn == null) {
            connect();
        } else {
            disconnect();
        }
        update_ui();
        return false;
    });
    $('#send').click(function() {
        var text = $('#text').val();
        var spam_num = $('#spam_num').val();
        var message = text.concat(':',spam_num);
        log('Sending: ' + message);
        conn.send(message);
        $('#text').val('').focus();
        return false;
    });
        
    $('#text').keyup(function(e) {
        if (e.keyCode === 13) {
            $('#send').click();
            return false;
        }
    });

});
