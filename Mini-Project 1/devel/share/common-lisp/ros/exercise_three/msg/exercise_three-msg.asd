
(cl:in-package :asdf)

(defsystem "exercise_three-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "UserInfo" :depends-on ("_package_UserInfo"))
    (:file "_package_UserInfo" :depends-on ("_package"))
  ))