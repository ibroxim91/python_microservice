until busybox nc -z "$host" 5672; do
  echo "RabbitMQ kutilyapti..."
  sleep 2
done
