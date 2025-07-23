from database.base_connection import BaseConnection
import psycopg2.extras


class Schedules(BaseConnection):
    def __init__(self):
        super().__init__(collection_name='schedules')

    def get_schedule(self, schedule_id):
        try:
            with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM schedules WHERE id = %s", (schedule_id,))
                result = cur.fetchone()
                return [dict(result)] if result else []
        except Exception as e:
            print(f"Error getting schedule: {e}")
            return []

    def delete_schedule(self, schedule_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM schedules WHERE id = %s", (schedule_id,))
        except Exception as e:
            print(f"Error deleting schedule: {e}")

    def add_schedule(self, schedule_id, interval):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO schedules (id, interval) VALUES (%s, %s) ON CONFLICT (id) DO UPDATE SET interval = EXCLUDED.interval",
                    (schedule_id, interval)
                )
        except Exception as e:
            print(f"Error adding schedule: {e}")

    def get_all_schedules(self):
        try:
            with self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT id as _id, interval FROM schedules")
                return [dict(row) for row in cur.fetchall()]
        except Exception as e:
            print(f"Error getting all schedules: {e}")
            return []
