
FROM postgres:alpine
RUN sh -c "for each in /docker-entrypoint/*.sh ; do sh $each ; done"