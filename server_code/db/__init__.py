import anvil.server
import psycopg2
from psycopg2.extras import RealDictCursor

# Get connection string from Anvil Secrets
@anvil.server.callable
def getconn(x='conn'):
  try:
    x=anvil.server.cookies.shared[x]
  except:
    x=''
  if x:
    return x
  else:
    return ''
    
@anvil.server.callable
def conn(x,y='conn'):
  anvil.server.cookies.shared[y]=x

def get_connection(x):
  # SSL mode 'require' is mandatory for Neon
  return psycopg2.connect(x, sslmode='require')

@anvil.server.callable
def execute_query(db, query, params=None):
  """Executes a SQL query and returns results as a list of dicts."""
  try:
    with get_connection(db) as conn:
      with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(query, params)
        if cur.description: # If query returns data (like SELECT)
          return list(cur.fetchall())
        conn.commit()
        return "Success"
  except Exception as e:
    return f"Error: {str(e)}"

@anvil.server.callable
def update_row(db, table, column, value, row_id):
  """Specific function for an editor to update a cell."""
  query = f"UPDATE {table} SET {column} = %s WHERE id = %s"
  return execute_query(db, query, (value, row_id))
