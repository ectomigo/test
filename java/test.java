public class Test {
	private final String aQuery = "SELECT o.id, o.val, t.id, t.val FROM one AS o CROSS JOIN two t";

	public void test() {
		Connection conn = Utils.getConn("test");
		PreparedStatement stmt = null;
		ResultSet rs = null;

		try {
			String strQuery =
				"UPDATE one " +
				"  SET val = ? " +
				"WHERE id = ?";

			StringBuilder sbQuery = new StringBuilder();

			sbQuery.append("UPDATE two ");
			sbQuery.append("  SET val = ?");
			sbQuery.append("WHERE id = ?");

			stmt = conn.prepareStatement(strQuery);
			stmt.setObject(1, "one-val");
			stmt.setObject(2, 1);
			stmt.execute();

			stmt = conn.prepareStatement(sbQuery);
			stmt.setObject(1, "two-val");
			stmt.setObject(2, 1);
			stmt.execute();
		} catch (SQLException ex) {
			throw new RuntimeException(ex.getMessage(), ex);
		} finally {
			Utils.closeQuietly(conn, stmt, rs);
		}
	}
}
