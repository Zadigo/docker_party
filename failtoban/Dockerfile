FROM superitman/fail2ban

LABEL "com.failtoban.app"="fail2ban"

COPY jail.local .

RUN touch auth.log && touch error.log