
import socket

class Context:
    def __init__(self, context):
        self.__dict__.update(context)

def p(*args):
    p.lines.append(' '.join([str(t) for t in args]))

def rerepl(context, addr='0.0.0.0', port=0):
    # pylint: disable=unused-variable
    # pylint: disable=broad-except
    # pylint: disable=exec-used
    af = socket.AF_INET if addr.count('.') == 3 else socket.AF_INET6
    sl = socket.socket(af, socket.SOCK_STREAM, 0)
    sl.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sl.settimeout(None)
    sl.bind((addr, port))
    sl.listen(1)
    print('Listening  at  ', sl.getsockname())
    conn, addr = sl.accept()
    print('Connection from', addr)
    conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    ctx = Context(context)
    buf = b''
    p.lines = []
    while True:
        ret = conn.recv(1024)
        if not ret:
            break
        buf += ret
        if buf[-2:] == b'\n\n' or buf[-2:] == b'\r\r' or buf[-3:] == b'\n\r\n':
            code = buf.decode('utf-8')
            buf  = b''
            try:
                exec(code)
            except Exception as e:
                conn.sendall((str(e) + '\r\n\r\n').encode('utf-8'))
            conn.sendall(('\r\n'.join(p.lines) + '\r\n\r\n').encode('utf-8'))
            p.lines = []

