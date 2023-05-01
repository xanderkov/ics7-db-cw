CREATE FUNCTION check_location() RETURNS TRIGGER AS $$
BEGIN
  IF NEW.location = '0 0' THEN
    RAISE NOTICE 'New visitor added with location: %', NEW.location;
    Return NEW;
  ELSE
    RETURN NULL;
  END IF;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER check_location_trigger
AFTER UPDATE ON "Visitor"
FOR EACH ROW
EXECUTE FUNCTION check_location();


DROP FUNCTION IF EXISTS check_location();

DROP TRIGGER IF EXISTS check_location_trigger ON "Visitor";