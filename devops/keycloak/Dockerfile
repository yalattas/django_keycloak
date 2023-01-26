FROM quay.io/keycloak/keycloak:18.0 as builder
ARG KEYCLOAK_HOME="/opt/keycloak"
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true
ENV KC_FEATURES="account-api,account2,admin2,authorization,ciba,client-policies,impersonation,par,step-up-authentication,web-authn,docker"
ENV KC_DB=postgres
# Install custom providers
RUN curl -sL https://github.com/aerogear/keycloak-metrics-spi/releases/download/2.5.3/keycloak-metrics-spi-2.5.3.jar -o ${KEYCLOAK_HOME}/providers/keycloak-metrics-spi-2.5.3.jar
RUN ${KEYCLOAK_HOME}/bin/kc.sh build

FROM quay.io/keycloak/keycloak:latest
ARG KEYCLOAK_HOME="/opt/keycloak"
COPY --from=builder ${KEYCLOAK_HOME}/ ${KEYCLOAK_HOME}/
WORKDIR ${KEYCLOAK_HOME}
# for demonstration purposes only, please make sure to use proper certificates in production instead
RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
RUN export PATH=$PATH:${KEYCLOAK_HOME}/bin
# change these values to point to a running postgres instance
ENV KC_DB_URL=db_url
ENV KC_DB_USERNAME=db_username
ENV KC_DB_PASSWORD=db_password
ENV KC_HOSTNAME=localhost
EXPOSE 8443
ENTRYPOINT ["bin/kc.sh"]
CMD ["start"]