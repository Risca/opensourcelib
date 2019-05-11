package com.zenterio.jenkins.postbuild

import com.zenterio.jenkins.scriptlet.IScriptlet
import com.zenterio.jenkins.scriptlet.TemplateScriptlet

import static com.zenterio.jenkins.scriptlet.Token.escape
import static com.zenterio.jenkins.scriptlet.Token.groovyToken


class CollectArtifactsScriptlet extends TemplateScriptlet {

    public CollectArtifactsScriptlet(IScriptlet template,
                                             String topJobName,
                                             String topBuildNumber,
                                             String iconPath) {
        super(template)
        this.addMacroDefinitions([
                (groovyToken("TOP_JOB_NAME")): escape(topJobName),
                (groovyToken("TOP_BUILD_NUMBER")): escape(topBuildNumber),
                (groovyToken("ICON")): escape(iconPath)
        ])
    }
}
