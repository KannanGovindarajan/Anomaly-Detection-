
LOGGING_FORMAT = '%(asctime)s %(name)s %(message)s'

def get_kdd_schema_text():
    """Based on http://kdd.ics.uci.edu/databases/kddcup99/kddcup.names"""
    return """duration: continuous.
protocol_type: string.
service: string.
flag: string.
src_bytes: continuous.
dst_bytes: continuous.
land: symbolic.
wrong_fragment: continuous.
urgent: continuous.
hot: continuous.
num_failed_logins: continuous.
logged_in: symbolic.
num_compromised: continuous.
root_shell: continuous.
su_attempted: continuous.
num_root: continuous.
num_file_creations: continuous.
num_shells: continuous.
num_access_files: continuous.
num_outbound_cmds: continuous.
is_host_login: symbolic.
is_guest_login: symbolic.
count: continuous.
srv_count: continuous.
serror_rate: continuous.
srv_serror_rate: continuous.
rerror_rate: continuous.
srv_rerror_rate: continuous.
same_srv_rate: continuous.
diff_srv_rate: continuous.
srv_diff_host_rate: continuous.
dst_host_count: continuous.
dst_host_srv_count: continuous.
dst_host_same_srv_rate: continuous.
dst_host_diff_srv_rate: continuous.
dst_host_same_src_port_rate: continuous.
dst_host_srv_diff_host_rate: continuous.
dst_host_serror_rate: continuous.
dst_host_srv_serror_rate: continuous.
dst_host_rerror_rate: continuous.
dst_host_srv_rerror_rate: continuous.
label: string."""

def get_kdd_feature_cols():
	"""Return list of columns that will be used as features in the ML algorithm."""
	return [
		'duration',
		'src_bytes',
		'dst_bytes',
		'land',
		'wrong_fragment',
		'urgent',
		'hot',
		'num_failed_logins',
		'logged_in',
		'num_compromised',
		'root_shell',
		'su_attempted',
		'num_root',
		'num_file_creations',
		'num_shells',
		'num_access_files',
		'num_outbound_cmds',
		'is_host_login',
		'is_guest_login',
		'count',
		'srv_count',
		'serror_rate',
		'srv_serror_rate',
		'rerror_rate',
		'srv_rerror_rate',
		'same_srv_rate',
		'diff_srv_rate',
		'srv_diff_host_rate',
		'dst_host_count',
		'dst_host_srv_count',
		'dst_host_same_srv_rate',
		'dst_host_diff_srv_rate',
		'dst_host_same_src_port_rate',
		'dst_host_srv_diff_host_rate',
		'dst_host_serror_rate',
		'dst_host_srv_serror_rate',
		'dst_host_rerror_rate',
		'dst_host_srv_rerror_rate']
